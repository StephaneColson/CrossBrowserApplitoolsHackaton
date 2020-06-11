def test_my_website(py):
    assert py.visit('https://demo.applitools.com/gridHackathonV1.html').title()\
           == 'Applitools UltraFastGrid | Cross Browser Testing Demo App'