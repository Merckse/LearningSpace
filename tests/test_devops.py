"""
Tests for DevOps tasks structure

These tests validate that the DevOps task modules are properly structured
and contain the expected task definitions.

Note: These tasks are instructional and meant to be completed manually,
so we test structure rather than functionality.
"""

import pytest
import sys
from pathlib import Path

# Add tasks directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'tasks'))

from devops import docker_basics, dockerfile_tasks, docker_compose_tasks, makefile_tasks


class TestDockerBasics:
    """Test Docker basics task structure"""
    
    def test_docker_basics_class_exists(self):
        """Verify DockerBasicsTasks class exists"""
        assert hasattr(docker_basics, 'DockerBasicsTasks')
    
    def test_docker_basics_has_tasks(self):
        """Verify DockerBasicsTasks has task methods"""
        tasks_class = docker_basics.DockerBasicsTasks
        task_methods = [
            'task_1_hello_world',
            'task_2_interactive_ubuntu',
            'task_3_nginx_web_server',
            'task_4_volume_mounting',
            'task_5_environment_variables',
            'task_6_image_management',
            'task_7_container_inspection',
            'task_8_cleanup'
        ]
        for method in task_methods:
            assert hasattr(tasks_class, method), f"Missing method: {method}"
    
    def test_docker_basics_has_reference(self):
        """Verify helper function exists"""
        assert hasattr(docker_basics, 'get_docker_commands_reference')
        reference = docker_basics.get_docker_commands_reference()
        assert isinstance(reference, dict)
        assert len(reference) > 0
    
    def test_docker_basics_has_instructions(self):
        """Verify instructions exist"""
        assert hasattr(docker_basics, 'INSTRUCTIONS')
        assert len(docker_basics.INSTRUCTIONS) > 0


class TestDockerfileTasks:
    """Test Dockerfile tasks structure"""
    
    def test_dockerfile_class_exists(self):
        """Verify DockerfileTasks class exists"""
        assert hasattr(dockerfile_tasks, 'DockerfileTasks')
    
    def test_dockerfile_has_tasks(self):
        """Verify DockerfileTasks has task methods"""
        tasks_class = dockerfile_tasks.DockerfileTasks
        task_methods = [
            'task_1_simple_python_app',
            'task_2_app_with_dependencies',
            'task_3_flask_web_app',
            'task_4_multi_stage_build',
            'task_5_environment_variables',
            'task_6_non_root_user',
            'task_7_dockerignore',
            'task_8_health_check'
        ]
        for method in task_methods:
            assert hasattr(tasks_class, method), f"Missing method: {method}"
    
    def test_dockerfile_has_best_practices(self):
        """Verify best practices helper exists"""
        assert hasattr(dockerfile_tasks, 'get_dockerfile_best_practices')
        practices = dockerfile_tasks.get_dockerfile_best_practices()
        assert isinstance(practices, dict)
        assert 'Security' in practices
        assert 'Efficiency' in practices
    
    def test_dockerfile_has_instructions(self):
        """Verify instructions exist"""
        assert hasattr(dockerfile_tasks, 'INSTRUCTIONS')
        assert len(dockerfile_tasks.INSTRUCTIONS) > 0


class TestDockerComposeTasks:
    """Test Docker Compose tasks structure"""
    
    def test_docker_compose_class_exists(self):
        """Verify DockerComposeTasks class exists"""
        assert hasattr(docker_compose_tasks, 'DockerComposeTasks')
    
    def test_docker_compose_has_tasks(self):
        """Verify DockerComposeTasks has task methods"""
        tasks_class = docker_compose_tasks.DockerComposeTasks
        task_methods = [
            'task_1_simple_web_app',
            'task_2_app_with_database',
            'task_3_development_environment',
            'task_4_multi_tier_application',
            'task_5_environment_files',
            'task_6_networking',
            'task_7_scaling_services',
            'task_8_production_setup'
        ]
        for method in task_methods:
            assert hasattr(tasks_class, method), f"Missing method: {method}"
    
    def test_docker_compose_has_commands(self):
        """Verify commands helper exists"""
        assert hasattr(docker_compose_tasks, 'get_docker_compose_commands')
        commands = docker_compose_tasks.get_docker_compose_commands()
        assert isinstance(commands, dict)
        assert len(commands) > 0
    
    def test_docker_compose_has_instructions(self):
        """Verify instructions exist"""
        assert hasattr(docker_compose_tasks, 'INSTRUCTIONS')
        assert len(docker_compose_tasks.INSTRUCTIONS) > 0


class TestMakefileTasks:
    """Test Makefile tasks structure"""
    
    def test_makefile_class_exists(self):
        """Verify MakefileTasks class exists"""
        assert hasattr(makefile_tasks, 'MakefileTasks')
    
    def test_makefile_has_tasks(self):
        """Verify MakefileTasks has task methods"""
        tasks_class = makefile_tasks.MakefileTasks
        task_methods = [
            'task_1_hello_makefile',
            'task_2_python_project',
            'task_3_dependencies',
            'task_4_variables',
            'task_5_pattern_rules',
            'task_6_docker_integration',
            'task_7_conditional_execution',
            'task_8_complete_project'
        ]
        for method in task_methods:
            assert hasattr(tasks_class, method), f"Missing method: {method}"
    
    def test_makefile_has_best_practices(self):
        """Verify best practices helper exists"""
        assert hasattr(makefile_tasks, 'get_makefile_best_practices')
        practices = makefile_tasks.get_makefile_best_practices()
        assert isinstance(practices, dict)
        assert 'Structure' in practices
        assert 'Variables' in practices
    
    def test_makefile_has_instructions(self):
        """Verify instructions exist"""
        assert hasattr(makefile_tasks, 'INSTRUCTIONS')
        assert len(makefile_tasks.INSTRUCTIONS) > 0


class TestDevOpsTasksDocumentation:
    """Test that all tasks have proper documentation"""
    
    def test_all_tasks_have_docstrings(self):
        """Verify all task methods have docstrings"""
        modules = [
            (docker_basics, 'DockerBasicsTasks'),
            (dockerfile_tasks, 'DockerfileTasks'),
            (docker_compose_tasks, 'DockerComposeTasks'),
            (makefile_tasks, 'MakefileTasks')
        ]
        
        for module, class_name in modules:
            tasks_class = getattr(module, class_name)
            for attr_name in dir(tasks_class):
                if attr_name.startswith('task_'):
                    method = getattr(tasks_class, attr_name)
                    assert method.__doc__ is not None, \
                        f"{class_name}.{attr_name} missing docstring"
                    assert len(method.__doc__.strip()) > 50, \
                        f"{class_name}.{attr_name} docstring too short"
    
    def test_module_docstrings_exist(self):
        """Verify all modules have docstrings"""
        modules = [docker_basics, dockerfile_tasks, docker_compose_tasks, makefile_tasks]
        for module in modules:
            assert module.__doc__ is not None
            assert len(module.__doc__.strip()) > 20


class TestDevOpsTasksStructure:
    """Test overall structure of devops tasks"""
    
    def test_all_tasks_are_static_methods(self):
        """Verify task methods are static"""
        modules = [
            (docker_basics, 'DockerBasicsTasks'),
            (dockerfile_tasks, 'DockerfileTasks'),
            (docker_compose_tasks, 'DockerComposeTasks'),
            (makefile_tasks, 'MakefileTasks')
        ]
        
        for module, class_name in modules:
            tasks_class = getattr(module, class_name)
            for attr_name in dir(tasks_class):
                if attr_name.startswith('task_'):
                    method = getattr(tasks_class, attr_name)
                    # Static methods are callable directly from class
                    assert callable(method)
    
    def test_task_numbering_is_sequential(self):
        """Verify tasks are numbered sequentially"""
        modules = [
            (docker_basics, 'DockerBasicsTasks'),
            (dockerfile_tasks, 'DockerfileTasks'),
            (docker_compose_tasks, 'DockerComposeTasks'),
            (makefile_tasks, 'MakefileTasks')
        ]
        
        for module, class_name in modules:
            tasks_class = getattr(module, class_name)
            task_names = [attr for attr in dir(tasks_class) if attr.startswith('task_')]
            task_numbers = []
            for name in task_names:
                # Extract number from task_N_name format
                parts = name.split('_')
                if len(parts) >= 2 and parts[1].isdigit():
                    task_numbers.append(int(parts[1]))
            
            # Verify sequential numbering
            task_numbers.sort()
            for i, num in enumerate(task_numbers, start=1):
                assert num == i, f"{class_name} tasks not sequential: missing task_{i}"
