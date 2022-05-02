
import os
import pytest

from app.spotify_service import artist_recommendation


CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_reccommendations():
    #with valid name, returns the reccommended artists and songs:
    results,artist_name = artist_recommendation("Dua Lipa")
    assert artist_name == 'Dua Lipa'
    artist_type = isinstance(artist_name, str)
    assert artist_type == True

    #results = artist_recommendation("Dua Lipa")
    recommendation_type = isinstance(results, list)
    assert recommendation_type == True
    
    related_count = len(results)
    assert related_count == 5

    related_artist = results[0]
    assert isinstance(related_artist, dict)
    keys = list(related_artist.keys())
    assert keys == ['names', 'display_images', 'songs']
