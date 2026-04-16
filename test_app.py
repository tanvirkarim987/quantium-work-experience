from app import app

# Test 1: Verify the header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    # dash_duo.wait_for_element looks for a CSS selector. 
    # 'h1' matches your header.
    header = dash_duo.wait_for_element("h1", timeout=10)
    assert header.text == "Pink Morsel Sales Data"

# Test 2: Verify the visualisation is present
def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    # We look for the ID we gave the dcc.Graph
    visualization = dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert visualization is not None

# Test 3: Verify the region picker is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    # We look for the ID we gave the dcc.RadioItems
    region_picker = dash_duo.wait_for_element("#region-filter", timeout=10)
    assert region_picker is not None