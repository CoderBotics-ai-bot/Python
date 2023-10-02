#
#from requests.exceptions import RequestException
#from urllib.error import HTTPError
#from requests.exceptions import RequestException
#
#import pytest
#from unittest.mock import Mock, patch
#from bs4 import BeautifulSoup
#from web_programming.fetch_well_rx_price import *
#
#
#from unittest.mock import patch
#
#
#def test_fetch_pharmacy_and_price_list_no_errors_with_value():
#    html_response = "<html><div class='grid-x pharmCard'><p class='list-title'>Pharmacy</p><span class='p price price-large'>$10</span></div></html>"
#
#    with patch("requests.get") as mock_get:
#        mock_get.return_value.text = html_response
#        mock_get.return_value.raise_for_status.return_value = None
#
#        result = fetch_pharmacy_and_price_list("drug_name", "zip_code")
#        assert result != None
#        assert type(result) == list
#        assert len(result) > 0
#        for pharmacy_price in result:
#            assert "pharmacy_name" in pharmacy_price
#            assert "price" in pharmacy_price
#
#
#def test_fetch_pharmacy_and_price_list_no_errors_with_no_value():
#    html_response = "<html></html>"
#
#    with patch("requests.get") as mock_get:
#        mock_get.return_value.text = html_response
#        mock_get.return_value.raise_for_status.return_value = None
#
#        result = fetch_pharmacy_and_price_list("drug_name", "zip_code")
#        assert result != None
#        assert type(result) == list
#        assert len(result) == 0
#
#
#def test_fetch_pharmacy_and_price_list_missing_inputs():
#    result = fetch_pharmacy_and_price_list(None, "zip_code")
#    assert result is None
#
#    result = fetch_pharmacy_and_price_list("drug_name", None)
#    assert result is None
#
#
#def test_fetch_pharmacy_and_price_list_http_error():
#    with patch("requests.get") as mock_get:
#        mock_get.return_value.raise_for_status.side_effect = HTTPError(
#            "url", "msg", "hdr", "fp"
#        )
#
#        result = fetch_pharmacy_and_price_list("drug_name", "zip_code")
#        assert result is None
#
#
#def test_fetch_pharmacy_and_price_list_request_exception():
#    with patch("requests.get") as mock_get:
#        mock_get.return_value.raise_for_status.side_effect = RequestException()
#
#        result = fetch_pharmacy_and_price_list("drug_name", "zip_code")
#        assert result is None
#