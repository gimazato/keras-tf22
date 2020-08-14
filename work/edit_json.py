import json

input_json_file_path = '/work/home/annotations/instances_val2017.json'
output_json_file_path = '~/work/home/instances_val2017-edit_test.json'

def edit_json(input_file_path, output_file_path):

    with open(file_path) as f:
        dict_of_json = json.load(f)
        
        # imagesのfile_nameを変更
        for i, image_dict in enumerate(dict_of_json["images"]):
            image_dict["file_name"] = "test{0}".format(str(i))

    with open(output_file_path, 'w') as f2:
        json.dump(dict_of_json, output_file_path)

edit_json(input_json_file_path, output_json_file_path)    