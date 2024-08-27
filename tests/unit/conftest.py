from collections import namedtuple
from comprasnet.pages.auction_minutes import AuctionMinutes
from unittest import mock
import pytest
import os

@pytest.fixture
def auction_minute():
    with mock.patch('comprasnet.pages.auction_minutes.requests.get') as mock_get:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '../assets/result_minutes_auction.html')
        MockResponse = namedtuple('Response', 'status_code, text')
        mock_response = MockResponse(status_code=200, text=open(path).read())
        mock_get.return_value = mock_response
        return AuctionMinutes(1234, 987)
