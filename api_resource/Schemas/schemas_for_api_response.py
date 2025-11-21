statement_card_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "session_uuid": {
                    "type": "string"
                },
                "action_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "type": "string"
                },
                "created_at": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                }
            },
            "required": [
                "session_uuid",
                "action_id",
                "updated_at",
                "created_at",
                "id"
            ]
        }
    },
    "required": [
        "data"
    ]
}

search_organizations_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "suggestions": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "unrestricted_value": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "kpp": {
                                    "type": "string"
                                },
                                "kpp_largest": {
                                    "type": "null"
                                },
                                "capital": {
                                    "type": "null"
                                },
                                "invalid": {
                                    "type": "null"
                                },
                                "management": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "post": {
                                            "type": "string"
                                        },
                                        "start_date": {
                                            "type": "integer"
                                        },
                                        "disqualified": {
                                            "type": "null"
                                        }
                                    },
                                    "required": [
                                        "name",
                                        "post",
                                        "start_date",
                                        "disqualified"
                                    ]
                                },
                                "founders": {
                                    "type": "null"
                                },
                                "managers": {
                                    "type": "null"
                                },
                                "predecessors": {
                                    "type": "null"
                                },
                                "successors": {
                                    "type": "null"
                                },
                                "branch_type": {
                                    "type": "string"
                                },
                                "branch_count": {
                                    "type": "integer"
                                },
                                "source": {
                                    "type": "null"
                                },
                                "qc": {
                                    "type": "null"
                                },
                                "hid": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "state": {
                                    "type": "object",
                                    "properties": {
                                        "status": {
                                            "type": "string"
                                        },
                                        "code": {
                                            "type": "null"
                                        },
                                        "actuality_date": {
                                            "type": "integer"
                                        },
                                        "registration_date": {
                                            "type": "integer"
                                        },
                                        "liquidation_date": {
                                            "type": "null"
                                        }
                                    },
                                    "required": [
                                        "status",
                                        "code",
                                        "actuality_date",
                                        "registration_date",
                                        "liquidation_date"
                                    ]
                                },
                                "opf": {
                                    "type": "object",
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        },
                                        "code": {
                                            "type": "string"
                                        },
                                        "full": {
                                            "type": "string"
                                        },
                                        "short": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "type",
                                        "code",
                                        "full",
                                        "short"
                                    ]
                                },
                                "name": {
                                    "type": "object",
                                    "properties": {
                                        "full_with_opf": {
                                            "type": "string"
                                        },
                                        "short_with_opf": {
                                            "type": "string"
                                        },
                                        "latin": {
                                            "type": "null"
                                        },
                                        "full": {
                                            "type": "string"
                                        },
                                        "short": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "full_with_opf",
                                        "short_with_opf",
                                        "latin",
                                        "full",
                                        "short"
                                    ]
                                },
                                "inn": {
                                    "type": "string"
                                },
                                "ogrn": {
                                    "type": "string"
                                },
                                "okpo": {
                                    "type": "string"
                                },
                                "okato": {
                                    "type": "string"
                                },
                                "oktmo": {
                                    "type": "string"
                                },
                                "okogu": {
                                    "type": "string"
                                },
                                "okfs": {
                                    "type": "string"
                                },
                                "okved": {
                                    "type": "string"
                                },
                                "okveds": {
                                    "type": "null"
                                },
                                "authorities": {
                                    "type": "null"
                                },
                                "documents": {
                                    "type": "null"
                                },
                                "licenses": {
                                    "type": "null"
                                },
                                "finance": {
                                    "type": "object",
                                    "properties": {
                                        "tax_system": {
                                            "type": "null"
                                        },
                                        "income": {
                                            "type": "null"
                                        },
                                        "expense": {
                                            "type": "null"
                                        },
                                        "revenue": {
                                            "type": "null"
                                        },
                                        "debt": {
                                            "type": "null"
                                        },
                                        "penalty": {
                                            "type": "null"
                                        },
                                        "year": {
                                            "type": "null"
                                        }
                                    },
                                    "required": [
                                        "tax_system",
                                        "income",
                                        "expense",
                                        "revenue",
                                        "debt",
                                        "penalty",
                                        "year"
                                    ]
                                },
                                "address": {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "unrestricted_value": {
                                            "type": "string"
                                        },
                                        "invalidity": {
                                            "type": "null"
                                        },
                                        "data": {
                                            "type": "object",
                                            "properties": {
                                                "postal_code": {
                                                    "type": "string"
                                                },
                                                "country": {
                                                    "type": "string"
                                                },
                                                "country_iso_code": {
                                                    "type": "string"
                                                },
                                                "federal_district": {
                                                    "type": "string"
                                                },
                                                "region_fias_id": {
                                                    "type": "string"
                                                },
                                                "region_kladr_id": {
                                                    "type": "string"
                                                },
                                                "region_iso_code": {
                                                    "type": "string"
                                                },
                                                "region_with_type": {
                                                    "type": "string"
                                                },
                                                "region_type": {
                                                    "type": "string"
                                                },
                                                "region_type_full": {
                                                    "type": "string"
                                                },
                                                "region": {
                                                    "type": "string"
                                                },
                                                "area_fias_id": {
                                                    "type": "null"
                                                },
                                                "area_kladr_id": {
                                                    "type": "null"
                                                },
                                                "area_with_type": {
                                                    "type": "null"
                                                },
                                                "area_type": {
                                                    "type": "null"
                                                },
                                                "area_type_full": {
                                                    "type": "null"
                                                },
                                                "area": {
                                                    "type": "null"
                                                },
                                                "city_fias_id": {
                                                    "type": "string"
                                                },
                                                "city_kladr_id": {
                                                    "type": "string"
                                                },
                                                "city_with_type": {
                                                    "type": "string"
                                                },
                                                "city_type": {
                                                    "type": "string"
                                                },
                                                "city_type_full": {
                                                    "type": "string"
                                                },
                                                "city": {
                                                    "type": "string"
                                                },
                                                "city_area": {
                                                    "type": "string"
                                                },
                                                "city_district_fias_id": {
                                                    "type": "null"
                                                },
                                                "city_district_kladr_id": {
                                                    "type": "null"
                                                },
                                                "city_district_with_type": {
                                                    "type": "string"
                                                },
                                                "city_district_type": {
                                                    "type": "string"
                                                },
                                                "city_district_type_full": {
                                                    "type": "string"
                                                },
                                                "city_district": {
                                                    "type": "string"
                                                },
                                                "settlement_fias_id": {
                                                    "type": "null"
                                                },
                                                "settlement_kladr_id": {
                                                    "type": "null"
                                                },
                                                "settlement_with_type": {
                                                    "type": "null"
                                                },
                                                "settlement_type": {
                                                    "type": "null"
                                                },
                                                "settlement_type_full": {
                                                    "type": "null"
                                                },
                                                "settlement": {
                                                    "type": "null"
                                                },
                                                "street_fias_id": {
                                                    "type": "string"
                                                },
                                                "street_kladr_id": {
                                                    "type": "string"
                                                },
                                                "street_with_type": {
                                                    "type": "string"
                                                },
                                                "street_type": {
                                                    "type": "string"
                                                },
                                                "street_type_full": {
                                                    "type": "string"
                                                },
                                                "street": {
                                                    "type": "string"
                                                },
                                                "stead_fias_id": {
                                                    "type": "null"
                                                },
                                                "stead_cadnum": {
                                                    "type": "null"
                                                },
                                                "stead_type": {
                                                    "type": "null"
                                                },
                                                "stead_type_full": {
                                                    "type": "null"
                                                },
                                                "stead": {
                                                    "type": "null"
                                                },
                                                "house_fias_id": {
                                                    "type": "string"
                                                },
                                                "house_kladr_id": {
                                                    "type": "string"
                                                },
                                                "house_cadnum": {
                                                    "type": "string"
                                                },
                                                "house_flat_count": {
                                                    "type": "null"
                                                },
                                                "house_type": {
                                                    "type": "string"
                                                },
                                                "house_type_full": {
                                                    "type": "string"
                                                },
                                                "house": {
                                                    "type": "string"
                                                },
                                                "block_type": {
                                                    "type": "null"
                                                },
                                                "block_type_full": {
                                                    "type": "null"
                                                },
                                                "block": {
                                                    "type": "null"
                                                },
                                                "entrance": {
                                                    "type": "null"
                                                },
                                                "floor": {
                                                    "type": "null"
                                                },
                                                "flat_fias_id": {
                                                    "type": "null"
                                                },
                                                "flat_cadnum": {
                                                    "type": "null"
                                                },
                                                "flat_type": {
                                                    "type": "string"
                                                },
                                                "flat_type_full": {
                                                    "type": "string"
                                                },
                                                "flat": {
                                                    "type": "string"
                                                },
                                                "flat_area": {
                                                    "type": "string"
                                                },
                                                "square_meter_price": {
                                                    "type": "string"
                                                },
                                                "flat_price": {
                                                    "type": "null"
                                                },
                                                "room_fias_id": {
                                                    "type": "null"
                                                },
                                                "room_cadnum": {
                                                    "type": "null"
                                                },
                                                "room_type": {
                                                    "type": "null"
                                                },
                                                "room_type_full": {
                                                    "type": "null"
                                                },
                                                "room": {
                                                    "type": "null"
                                                },
                                                "postal_box": {
                                                    "type": "null"
                                                },
                                                "fias_id": {
                                                    "type": "string"
                                                },
                                                "fias_code": {
                                                    "type": "string"
                                                },
                                                "fias_level": {
                                                    "type": "string"
                                                },
                                                "fias_actuality_state": {
                                                    "type": "string"
                                                },
                                                "kladr_id": {
                                                    "type": "string"
                                                },
                                                "geoname_id": {
                                                    "type": "string"
                                                },
                                                "capital_marker": {
                                                    "type": "string"
                                                },
                                                "okato": {
                                                    "type": "string"
                                                },
                                                "oktmo": {
                                                    "type": "string"
                                                },
                                                "tax_office": {
                                                    "type": "string"
                                                },
                                                "tax_office_legal": {
                                                    "type": "string"
                                                },
                                                "timezone": {
                                                    "type": "string"
                                                },
                                                "geo_lat": {
                                                    "type": "string"
                                                },
                                                "geo_lon": {
                                                    "type": "string"
                                                },
                                                "beltway_hit": {
                                                    "type": "string"
                                                },
                                                "beltway_distance": {
                                                    "type": "null"
                                                },
                                                "metro": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "name": {
                                                                    "type": "string"
                                                                },
                                                                "line": {
                                                                    "type": "string"
                                                                },
                                                                "distance": {
                                                                    "type": "number"
                                                                }
                                                            },
                                                            "required": [
                                                                "name",
                                                                "line",
                                                                "distance"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "name": {
                                                                    "type": "string"
                                                                },
                                                                "line": {
                                                                    "type": "string"
                                                                },
                                                                "distance": {
                                                                    "type": "number"
                                                                }
                                                            },
                                                            "required": [
                                                                "name",
                                                                "line",
                                                                "distance"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "name": {
                                                                    "type": "string"
                                                                },
                                                                "line": {
                                                                    "type": "string"
                                                                },
                                                                "distance": {
                                                                    "type": "number"
                                                                }
                                                            },
                                                            "required": [
                                                                "name",
                                                                "line",
                                                                "distance"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "divisions": {
                                                    "type": "null"
                                                },
                                                "qc_geo": {
                                                    "type": "string"
                                                },
                                                "qc_complete": {
                                                    "type": "null"
                                                },
                                                "qc_house": {
                                                    "type": "null"
                                                },
                                                "history_values": {
                                                    "type": "null"
                                                },
                                                "unparsed_parts": {
                                                    "type": "null"
                                                },
                                                "source": {
                                                    "type": "string"
                                                },
                                                "qc": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "postal_code",
                                                "country",
                                                "country_iso_code",
                                                "federal_district",
                                                "region_fias_id",
                                                "region_kladr_id",
                                                "region_iso_code",
                                                "region_with_type",
                                                "region_type",
                                                "region_type_full",
                                                "region",
                                                "area_fias_id",
                                                "area_kladr_id",
                                                "area_with_type",
                                                "area_type",
                                                "area_type_full",
                                                "area",
                                                "city_fias_id",
                                                "city_kladr_id",
                                                "city_with_type",
                                                "city_type",
                                                "city_type_full",
                                                "city",
                                                "city_area",
                                                "city_district_fias_id",
                                                "city_district_kladr_id",
                                                "city_district_with_type",
                                                "city_district_type",
                                                "city_district_type_full",
                                                "city_district",
                                                "settlement_fias_id",
                                                "settlement_kladr_id",
                                                "settlement_with_type",
                                                "settlement_type",
                                                "settlement_type_full",
                                                "settlement",
                                                "street_fias_id",
                                                "street_kladr_id",
                                                "street_with_type",
                                                "street_type",
                                                "street_type_full",
                                                "street",
                                                "stead_fias_id",
                                                "stead_cadnum",
                                                "stead_type",
                                                "stead_type_full",
                                                "stead",
                                                "house_fias_id",
                                                "house_kladr_id",
                                                "house_cadnum",
                                                "house_flat_count",
                                                "house_type",
                                                "house_type_full",
                                                "house",
                                                "block_type",
                                                "block_type_full",
                                                "block",
                                                "entrance",
                                                "floor",
                                                "flat_fias_id",
                                                "flat_cadnum",
                                                "flat_type",
                                                "flat_type_full",
                                                "flat",
                                                "flat_area",
                                                "square_meter_price",
                                                "flat_price",
                                                "room_fias_id",
                                                "room_cadnum",
                                                "room_type",
                                                "room_type_full",
                                                "room",
                                                "postal_box",
                                                "fias_id",
                                                "fias_code",
                                                "fias_level",
                                                "fias_actuality_state",
                                                "kladr_id",
                                                "geoname_id",
                                                "capital_marker",
                                                "okato",
                                                "oktmo",
                                                "tax_office",
                                                "tax_office_legal",
                                                "timezone",
                                                "geo_lat",
                                                "geo_lon",
                                                "beltway_hit",
                                                "beltway_distance",
                                                "metro",
                                                "divisions",
                                                "qc_geo",
                                                "qc_complete",
                                                "qc_house",
                                                "history_values",
                                                "unparsed_parts",
                                                "source",
                                                "qc"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "unrestricted_value",
                                        "invalidity",
                                        "data"
                                    ]
                                },
                                "phones": {
                                    "type": "null"
                                },
                                "emails": {
                                    "type": "null"
                                },
                                "ogrn_date": {
                                    "type": "integer"
                                },
                                "okved_type": {
                                    "type": "string"
                                },
                                "employee_count": {
                                    "type": "null"
                                }
                            },
                            "required": [
                                "kpp",
                                "kpp_largest",
                                "capital",
                                "invalid",
                                "management",
                                "founders",
                                "managers",
                                "predecessors",
                                "successors",
                                "branch_type",
                                "branch_count",
                                "source",
                                "qc",
                                "hid",
                                "type",
                                "state",
                                "opf",
                                "name",
                                "inn",
                                "ogrn",
                                "okpo",
                                "okato",
                                "oktmo",
                                "okogu",
                                "okfs",
                                "okved",
                                "okveds",
                                "authorities",
                                "documents",
                                "licenses",
                                "finance",
                                "address",
                                "phones",
                                "emails",
                                "ogrn_date",
                                "okved_type",
                                "employee_count"
                            ]
                        }
                    },
                    "required": [
                        "value",
                        "unrestricted_value",
                        "data"
                    ]
                }
            ]
        }
    },
    "required": [
        "suggestions"
    ]
}

exchange_rate_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "currency_from": {
                        "type": "string"
                    },
                    "currency_to": {
                        "type": "string"
                    },
                    "purchase": {
                        "type": "number"
                    },
                    "sell": {
                        "type": "number"
                    },
                    "ranges_from": {
                        "type": "object",
                        "properties": {
                            "from": {
                                "type": "number"
                            },
                            "to": {
                                "type": "number"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "from",
                            "to"
                        ]
                    },
                    "ranges_to": {
                        "type": "object",
                        "properties": {
                            "from": {
                                "type": "integer"
                            },
                            "to": {
                                "type": "integer"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "from",
                            "to"
                        ]
                    },
                    "is_cross_currency": {
                        "type": "boolean"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "currency_from",
                    "currency_to",
                    "purchase",
                    "sell",
                    "ranges_from",
                    "ranges_to",
                    "is_cross_currency"
                ]
            }
        }
    },
    "additionalProperties": False,
    "required": [
        "data"
    ]
}

subscription_service_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "parent_id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "published": {
                        "type": "boolean"
                    },
                    "alias": {
                        "type": "string"
                    },
                    "is_folder": {
                        "type": "boolean"
                    },
                    "sort": {
                        "type": "integer"
                    },
                    "content_id": {
                        "type": "integer"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "deleted_at": {
                        "type": "null"
                    },
                    "uri": {
                        "type": "string"
                    },
                    "content": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "longtitle": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "description": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "keywords": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "content": {
                                "type": "object",
                                "properties": {
                                    "time": {
                                        "type": "integer"
                                    },
                                    "blocks": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "data": {
                                                    "type": "object",
                                                    "properties": {
                                                        "text": {
                                                            "type": "string"
                                                        },
                                                        "items": {
                                                            "type": "array",
                                                            "items": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "style": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "additionalProperties": False
                                                },
                                                "type": {
                                                    "type": "string"
                                                }
                                            },
                                            "additionalProperties": False,
                                            "required": [
                                                "id",
                                                "data",
                                                "type"
                                            ]
                                        }
                                    },
                                    "version": {
                                        "type": "string"
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "time",
                                    "blocks",
                                    "version"
                                ]
                            },
                            "published": {
                                "type": "boolean"
                            },
                            "main_page_id": {
                                "type": "string"
                            },
                            "template_id": {
                                "type": "integer"
                            },
                            "fields": {
                                "type": "object",
                                "properties": {
                                    "tags": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "anyOf": [
                                                    {
                                                        "type": "null"
                                                    },
                                                    {
                                                        "type": "array",
                                                        "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                "label": {
                                                                    "type": "string"
                                                                },
                                                                "value": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                "label",
                                                                "value"
                                                            ]
                                                        }
                                                    }
                                                ]
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "microtags": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "image": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "preview": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "noindex": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "canonicalurl": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "icons": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": [
                                                    "string",
                                                    "null"
                                                ]
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "formid": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "link_access": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    },
                                    "shortname": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "null"
                                            }
                                        },
                                        "additionalProperties": False
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "tags",
                                    "microtags",
                                    "noindex",
                                    "canonicalurl"
                                ]
                            },
                            "files": {
                                "type": "array"
                            },
                            "template": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "title": {
                                        "type": "string"
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "id",
                                    "name",
                                    "title"
                                ]
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "id",
                            "title",
                            "keywords",
                            "content",
                            "published",
                            "main_page_id",
                            "template_id",
                            "fields",
                            "files",
                            "template"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "id",
                    "parent_id",
                    "title",
                    "published",
                    "alias",
                    "is_folder",
                    "sort",
                    "content_id",
                    "created_at",
                    "updated_at",
                    "uri",
                    "content"
                ]
            }
        }
    },
    "additionalProperties": False,
    "required": [
        "data"
    ]
}
