import os
import shutil
from mvcforge.generator import MVCProjectGenerator

def test_create_directories():
    project_name = "TestProject"
    generator = MVCProjectGenerator(project_name)
    generator.generate_project()
    
    assert os.path.exists(project_name)
    assert os.path.exists(os.path.join(project_name, 'models'))
    assert os.path.exists(os.path.join(project_name, 'views'))
    assert os.path.exists(os.path.join(project_name, 'controllers'))
    
    # Cleanup after test
    shutil.rmtree(project_name)
