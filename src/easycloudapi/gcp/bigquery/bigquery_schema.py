"""
Generate Bigquery Schema
-------------------------
This module to generate the Google Bigquery Schema

    # Creating a JSON schema file
    # Ref: https://cloud.google.com/bigquery/docs/schemas#creating_a_JSON_schema_file
    # test:
    # 1. https://transform.tools/json-to-big-query
    # 2. https://bigquery-json-schema-generator.com/

"""
import json


class BigquerySchema(object):
    """
    A class to generate Bigquery Schema
    ...

    :Attributes
    -----------
        col_name: str
            Bigquery Column Name
        col_type: str (default: "STRING")
            Bigquery Column Type 
        Column Type can be any one of ["STRING", "INTEGER", "DATE", "DATETIME", "record"]
            col_mode: str (default: "NULLABLE")
        Bigquery Column Mode 
            Column Mode can be one of ["NULLABLE", "repeated"]

    :Static Methods
    ---------------
        _get_generic_coloum_schema(col_name=<col_name>, col_type="STRING", col_mode="NULLABLE"):
            Generate Bigquery generic column schema

        generate_bq_schema(data=<json_data>):
            Generate Bigquery whole column schema
            
    """
    @staticmethod
    def _get_generic_coloum_schema(col_name: str, 
                                   col_type: str = "STRING", 
                                   col_mode: str = "NULLABLE"
                                   ) -> dict:
        """
        Generate Bigquery generic column schema

        This method is for internal functionality. 

        :param
        ------ 
            col_name: str 
            col_type: str (default: "STRING") 
            col_mode: str (default: "NULLABLE")

        :return
        -------
            generic bigquery column schema, list obj

        """
        generic_coloum_schema = {}
        generic_coloum_schema["name"] = col_name
        generic_coloum_schema["type"] = col_type
        if col_mode != "NULLABLE":
            generic_coloum_schema["mode"] = col_mode
        # generic_coloum_schema["description"] = "_" + col_name
        return generic_coloum_schema


    @staticmethod
    def generate_bq_schema(data: dict) -> list:
        """
        Generate Bigquery whole schema
        
        :param
        ------ 
            data: dict 

        :return
        -------
            bigquery column schema as a list object
        
        """
        out_schema = []
        for i, j in data.items():
            if type(j) == str:
                out_schema.append(
                    BigquerySchema._get_generic_coloum_schema(col_name=str(i))
                )
            elif type(j) == int:
                out_schema.append(
                    BigquerySchema._get_generic_coloum_schema(col_name=str(i), col_type="INTEGER")
                )
            elif type(j) == list:
                element = j[0]
                if type(element) == str:
                    out_schema.append(
                        BigquerySchema._get_generic_coloum_schema(col_name=str(i),
                                                                    col_mode="repeated")
                    )
                elif type(element) == int:
                    out_schema.append(
                        BigquerySchema._get_generic_coloum_schema(col_name=str(i),
                                                                    col_type="INTEGER",
                                                                    col_mode="repeated")
                    )
                elif type(element) == dict:
                    dict_obj = BigquerySchema._get_generic_coloum_schema(col_name=str(i),
                                                                           col_type="record")
                    dict_obj["fields"] = BigquerySchema.generate_bq_schema(element)
                    out_schema.append(dict_obj)
            elif type(j) == dict:
                dict_obj = BigquerySchema._get_generic_coloum_schema(col_name=str(i),
                                                                       col_type="record")
                dict_obj["fields"] = BigquerySchema.generate_bq_schema(j)
                out_schema.append(dict_obj)
            else:
                pass
        return out_schema


if __name__ == "__main__":
    bs = BigquerySchema()
    with open("tests//test_data//sample_json_01.json") as json_file:
        sample_dict = json.load(json_file)
    out = bs.generate_bq_schema(data=sample_dict)
    print(f"output from generate_bq_schema:\n{out}")
