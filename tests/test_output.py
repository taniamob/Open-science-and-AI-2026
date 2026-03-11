import os

def test_abstracts_file_exists():
    assert os.path.exists("outcome/abstracts.txt"), "abstracts.txt is missing"

def test_links_file_exists():
    assert os.path.exists("outcome/links.txt"), "links.txt is missing"

def test_keyword_cloud_exists():
    assert os.path.exists("outcome/keyword_cloud.png"), "keyword_cloud.png is missing"

def test_figure_plot_exists():
    assert os.path.exists("outcome/num_figures.png"), "num_figures.png is missing"