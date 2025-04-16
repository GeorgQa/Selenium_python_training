# -*- coding: utf-8 -*-
import pytest

from fixture.applications import Applications


@pytest.fixture
def app(request):
    fixture = Applications()
    request.addfinalizer(fixture.destroy)
    return  fixture

def test_add_group(app):
    app.open_home_page()
    app.session.login()
    app.create_group()
    app.filling_in_group_data( "new_group", "Header", "vtgtr")
    app.save()
    app.session.logout()

def test_no_data_group(app):
    app.open_home_page()
    app.session.login()
    app.create_group()
    app.filling_in_group_data( " ", " ", " ")
    app.save()
    app.session.logout()


