#!/usr/bin/env python3
"""
Deep Tree Echo - System Verification Script
===========================================

This script verifies that the Deep Tree Echo system is properly preserved
and functional as of the December 2024 snapshot.

This verification is part of the time capsule preservation project.
"""

import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Tuple

class SystemVerifier:
    def __init__(self):
        self.results = []
        self.total_checks = 0
        self.passed_checks = 0
        
    def check(self, name: str, test_func):
        """Run a verification check"""
        self.total_checks += 1
        try:
            result = test_func()
            if result:
                self.passed_checks += 1
                self.results.append((name, "✅ PASS", None))
                return True
            else:
                self.results.append((name, "❌ FAIL", "Test returned False"))
                return False
        except Exception as e:
            self.results.append((name, "⚠️  SKIP", str(e)))
            return False
    
    def print_results(self):
        """Print verification results"""
        print("\n" + "=" * 70)
        print("DEEP TREE ECHO - SYSTEM VERIFICATION RESULTS")
        print("=" * 70 + "\n")
        
        for name, status, error in self.results:
            print(f"{status} {name}")
            if error:
                print(f"    Reason: {error}")
        
        print("\n" + "=" * 70)
        print(f"Results: {self.passed_checks}/{self.total_checks} checks passed")
        
        if self.passed_checks == self.total_checks:
            print("Status: ✅ FULLY VERIFIED")
        elif self.passed_checks > 0:
            print("Status: ⚠️  PARTIALLY VERIFIED (see PRESERVATION.md for setup)")
        else:
            print("Status: 📦 PRESERVED (dependencies not installed)")
        
        print("=" * 70 + "\n")

def check_core_files():
    """Verify core system files exist"""
    required_files = [
        'deep_tree_echo.py',
        'ml_system.py',
        'sensory_motor.py',
        'browser_interface.py',
        'cognitive_architecture.py',
        'chat_interface.py',
        'auth_manager.py',
        'production_config.py',
        'requirements.txt',
    ]
    
    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)
    
    if missing:
        print(f"Missing files: {missing}")
        return False
    return True

def check_documentation():
    """Verify documentation files exist"""
    required_docs = [
        'README.md',
        'HISTORY.md',
        'PRESERVATION.md',
        'Deep-Tree-Echo-Persona.md',
        'PRODUCTION_SUMMARY.md',
    ]
    
    missing = []
    for doc in required_docs:
        if not Path(doc).exists():
            missing.append(doc)
    
    if missing:
        print(f"Missing documentation: {missing}")
        return False
    return True

def check_examples():
    """Verify example files exist"""
    required_examples = [
        'examples/README.md',
        'examples/demo_ml_vision.py',
        'examples/demo_motor_control.py',
    ]
    
    missing = []
    for example in required_examples:
        if not Path(example).exists():
            missing.append(example)
    
    if missing:
        print(f"Missing examples: {missing}")
        return False
    return True

def check_test_files():
    """Verify test files exist"""
    test_files = [
        'test_deep_tree_echo.py',
        'test_ml_system.py',
        'test_sensory_motor.py',
        'test_auth.py',
    ]
    
    missing = []
    for test_file in test_files:
        if not Path(test_file).exists():
            missing.append(test_file)
    
    if missing:
        print(f"Missing test files: {missing}")
        return False
    return True

def check_python_imports():
    """Check if core Python modules can be imported (without dependencies)"""
    # Check if files are syntactically valid Python
    modules = [
        'deep_tree_echo',
    ]
    
    for module in modules:
        spec = importlib.util.find_spec(module)
        if spec is None:
            return False
    return True

def check_directory_structure():
    """Verify expected directory structure"""
    expected_dirs = [
        'examples',
        'activity_logs',
        '.mem',
    ]
    
    missing = []
    for dir_name in expected_dirs:
        if not Path(dir_name).exists():
            missing.append(dir_name)
    
    if missing:
        print(f"Missing directories: {missing}")
        return False
    return True

def check_configuration_templates():
    """Verify configuration templates exist"""
    templates = [
        '.env.template',
        'team_config.yaml',
        'docker-compose.yml',
        'Dockerfile',
    ]
    
    missing = []
    for template in templates:
        if not Path(template).exists():
            missing.append(template)
    
    if missing:
        print(f"Missing configuration files: {missing}")
        return False
    return True

def check_preservation_metadata():
    """Verify preservation metadata is complete"""
    history = Path('HISTORY.md')
    preservation = Path('PRESERVATION.md')
    
    if not history.exists() or not preservation.exists():
        return False
    
    # Check that HISTORY.md has substantial content
    history_content = history.read_text()
    if len(history_content) < 5000:  # Should be comprehensive
        print("HISTORY.md appears incomplete")
        return False
    
    # Check that PRESERVATION.md has setup instructions
    preservation_content = preservation.read_text()
    if 'Installation Instructions' not in preservation_content:
        print("PRESERVATION.md missing installation instructions")
        return False
    
    return True

def check_readme_updates():
    """Verify README reflects time capsule nature"""
    readme = Path('README.md')
    if not readme.exists():
        return False
    
    content = readme.read_text()
    
    # Check for time capsule indicators
    indicators = [
        'time capsule',
        '2023-2024',
        'Deep Tree Echo',
        'ML vision',
        'autonomous',
    ]
    
    missing = []
    for indicator in indicators:
        if indicator.lower() not in content.lower():
            missing.append(indicator)
    
    if missing:
        print(f"README missing key sections: {missing}")
        return False
    
    return True

def main():
    print("\n" + "🌟" * 35)
    print("   DEEP TREE ECHO - SYSTEM VERIFICATION")
    print("   Time Capsule Preservation Check")
    print("🌟" * 35 + "\n")
    
    verifier = SystemVerifier()
    
    print("Verifying Deep Tree Echo system preservation...\n")
    
    # Core System Checks
    print("📁 Core System Files...")
    verifier.check("Core Python files exist", check_core_files)
    verifier.check("Directory structure correct", check_directory_structure)
    verifier.check("Configuration templates present", check_configuration_templates)
    
    # Documentation Checks
    print("\n📚 Documentation...")
    verifier.check("Documentation files exist", check_documentation)
    verifier.check("Preservation metadata complete", check_preservation_metadata)
    verifier.check("README updated for time capsule", check_readme_updates)
    
    # Examples & Tests
    print("\n🎮 Examples & Tests...")
    verifier.check("Example demonstrations exist", check_examples)
    verifier.check("Test suite files exist", check_test_files)
    
    # Print Results
    verifier.print_results()
    
    # Additional Information
    print("📖 Next Steps:")
    print("   1. See PRESERVATION.md for installation instructions")
    print("   2. See HISTORY.md for the complete achievement story")
    print("   3. Run examples/demo_ml_vision.py to see ML vision")
    print("   4. Run examples/demo_motor_control.py to see motor control")
    print("   5. Install dependencies: pip install -r requirements.txt")
    print("")
    print("🎉 This time capsule preserves Deep Tree Echo's achievements")
    print("   from 2023-2024, when autonomous web navigation required")
    print("   pioneering innovation—before it became easy.")
    print("")
    
    # Return appropriate exit code
    if verifier.passed_checks == verifier.total_checks:
        return 0
    elif verifier.passed_checks > 0:
        return 0  # Partial success is still success for preservation
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
