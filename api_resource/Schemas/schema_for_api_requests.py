statement_card_schema_request = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "action": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "action"
    ]
}

search_organizations_schema_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "query": {
            "type": "string"
        }
    },
    "required": [
        "query"
    ]
}

exchange_rate_schema_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "from": {
            "type": "string"
        },
        "to": {
            "type": "string"
        },
        "filter[type]": {
            "type": "string"
        },
        "filter[region]": {
            "type": "integer"
        }
    },
    "required": [
        "from",
        "to",
        "filter[type]",
        "filter[region]"
    ]
}
subscription_service_schema_request = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "depth": {
            "type": "integer"
        },
        "sort": {
            "type": "string"
        },
        "filter[content.fields.multiselect]": {
            "type": "string"
        },
        "filter[content.template.name]": {
            "type": "string"
        }
    },
    "required": [
        "depth",
        "sort",
        "filter[content.fields.multiselect]",
        "filter[content.template.name]"
    ]
}
