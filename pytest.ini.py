# content of pytest.ini
[pytest]
# Run firefox with UI
addopts = --headed
          --browser=chromium
          --tracing=retain-on-failure
          --video=retain-on-failure
          --screenshot=only-on-failure
          --reruns=2
          --reruns-delay=2
          #--slowmo=1000
