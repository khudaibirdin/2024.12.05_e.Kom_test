from app.internal.database import db
from app.internal.validation import Validation


def get_templates_name(input_data:dict) -> dict:
    # templates = db.all()
    # validator = Validation()
    # matches = True
    # for template in templates:
    #     for template_field_name, template_field_type in template.items():
    #         if template_field_name == "name":
    #             continue
    #         if template_field_name in input_data:
    #             value = input_data[template_field_name]
    #             value_type = validator.validate(value)
    #             if value_type != template_field_type:
    #                 matches = False
    #                 break
    #         else:
    #             matches = False
    #             break
    #     if matches:
    #         return {"template_name": template["name"]}
    # return {field_name: validator.validate(value) for field_name, value in input_data.items()}
    validator = Validation()
    suitable_templates = []
    for template in db.all():
        if set(input_data).issubset(template):
            suitable_templates.append(template)
    validated_templates = []
    for suitable_template in suitable_templates:
        is_valid = True
        for field_name, field_value in input_data.items():
            if validator.validate(field_value) != suitable_template[field_name]:
                is_valid = False
        if is_valid:
            validated_templates.append(suitable_template)
    if validated_templates:
        return {"template_name": suitable_templates[0]["name"]}
    return {field_name: validator.validate(value) for field_name, value in input_data.items()}
