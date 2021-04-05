

from app.Model import Model
from app.ParamView import ParamView

import pytest


def set_ots_info_list(ots_info_list, disable_base_param_edit=False):
    ots_id_param_views = []
    for ots_info_item in ots_info_list:
        ots_param_list = []
        for x in ots_info_item:
            if x['ParamDef'].title == 'OTS Id':
                print(f'{x["ParamDef"].title}: {x["ParamValue"]}')

            ots_param_list.append(ParamView(x['ParamDef'], x['ParamValue'], disable_base_param_edit))
        ots_id_param_views.append(ots_param_list)
    return ots_id_param_views


def print_packages_using_ots_id(model, ots_info_list):
    for ots_info_item in ots_info_list:
        for x in ots_info_item:
            if x['ParamDef'].title == 'OTS Id':
                ots_id = x["ParamValue"]
                print(f'TEST: {model.get_packages_using_ots_id(ots_id)}')


def print_ots_id_param_views(ots_id_param_views):
    for entry in ots_id_param_views:
        for x in entry:
            param_value = x.param_value
            title = x.param_def.title
            print(f'{title}: {param_value}')


def test_model():
    # model = Model.instance('Test_OTS_database.xlsx', is_trace=True)
    # model = Model.instance('OTS_database.xlsx', is_trace=True)
    model = Model.instance('OTS_database_dup.xlsx', is_trace=True)
    model.is_trace = True
    # ots_item_params_list = model.get_ots_item_params_list()
    # print_packages_using_ots_id(model, ots_item_params_list)
    # ots_id_param_views = set_ots_info_list(ots_item_params_list)
    # print_ots_id_param_views(ots_id_param_views)

    # if len(ots_item_params_list) == 0:
    #    pytest.fail('Failed...')
