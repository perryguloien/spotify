
import os
import pytest

from app.spotify_service import artist_recommendation


CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_reccommendations():
    #with valid name, returns the reccommended artists and songs:
    results,artist_name = artist_recommendation("Dua Lipa")
    assert name_res == 'Dua Lipa'
    
    breakpoint()
    #with invalid name, fails gracefully and returns nothing:
    invalid_results = artist_recommendation(name=129112)
    assert invalid_results == None

