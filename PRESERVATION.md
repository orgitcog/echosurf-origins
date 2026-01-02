# Deep Tree Echo - Preservation Metadata
## Time Capsule: December 2024 Snapshot

> **This document contains technical preservation information to ensure the Deep Tree Echo system can be restored and run in the future.**

---

## Preservation Date
- **Snapshot Date**: December 2024
- **Preservation Date**: January 2, 2026
- **Repository**: https://github.com/orgitcog/echosurf-origins
- **Preserved By**: GitHub Copilot Time Capsule Project

---

## System Snapshot Information

### Python Environment (December 2024)
```
Python Version: 3.12.3
Platform: Ubuntu 20.04 LTS (primary), Windows 10+ (supported)
Architecture: x86_64
```

### Core Dependencies (Exact Versions)
```
# Browser Automation
playwright==1.40.0
selenium==4.15.0
undetected-chromedriver==3.5.0

# Machine Learning & Computer Vision
tensorflow==2.16.0
opencv-python==4.8.0
scikit-learn==1.3.0
numpy==1.24.0
Pillow==10.0.0

# Human-like Interaction
pyautogui==0.9.54
pynput==1.7.6

# System & Utilities
psutil==5.9.0
requests==2.31.0
python-dotenv==1.0.0
beautifulsoup4==4.12.0
websockets==12.0

# Production Dependencies
cryptography==41.0.0
PyJWT==2.8.0
pyyaml==6.0
asyncio-mqtt==0.16.0
aioredis==2.0.0
sqlalchemy==2.0.0
alembic==1.12.0
prometheus-client==0.18.0
opentelemetry-api==1.20.0
opentelemetry-sdk==1.20.0
sentry-sdk==1.35.0
uvicorn==0.24.0
fastapi==0.104.0
pydantic==2.4.0
celery==5.3.0
redis==5.0.0
```

### System Libraries Required
```bash
# Ubuntu/Debian
sudo apt-get install -y \
    python3-tk \
    python3-dev \
    scrot \
    xdotool \
    libopencv-dev \
    firefox \
    xvfb \
    x11vnc
```

---

## Directory Structure

```
echosurf-origins/
├── .deep_tree_echo/              # User home directory runtime data
│   ├── ml/                       # ML models and training data
│   │   ├── activity.json
│   │   └── models/
│   ├── sensory/                  # Sensory-motor activity logs
│   │   └── activity.json
│   ├── cognitive/                # Cognitive architecture data
│   │   └── activity.json
│   ├── memories/                 # Persistent memory storage
│   └── firefox_profile/          # Browser profile data
│
├── Core Systems
│   ├── deep_tree_echo.py         # Main Echo State Network core
│   ├── ml_system.py              # ML vision and learning
│   ├── sensory_motor.py          # Human-like interaction
│   ├── browser_interface.py      # Browser automation
│   ├── cognitive_architecture.py # Memory and goal management
│   └── chat_interface.py         # Chat automation
│
├── Support Systems
│   ├── auth_manager.py           # Credential management
│   ├── production_config.py      # Configuration system
│   ├── monitor.py                # System monitoring
│   ├── activity_regulation.py    # Activity pacing
│   ├── activity_stream.py        # Activity logging
│   ├── emergency_protocols.py    # Error recovery
│   └── personality_system.py     # Personality traits
│
├── Interfaces
│   ├── selenium_interface.py     # Selenium browser control
│   ├── terminal_controller.py    # Terminal interaction
│   └── monitor_interface.py      # Monitoring UI
│
├── Configuration
│   ├── .env.template             # Environment variables template
│   ├── team_config.yaml          # Team configuration
│   ├── requirements.txt          # Python dependencies
│   └── docker-compose.yml        # Container orchestration
│
├── Tests
│   ├── test_deep_tree_echo.py    # Core system tests
│   ├── test_ml_system.py         # ML vision tests
│   ├── test_sensory_motor.py     # Interaction tests
│   ├── test_auth.py              # Authentication tests
│   └── test_echo.py              # Integration tests
│
├── Documentation
│   ├── README.md                 # Project overview
│   ├── HISTORY.md               # Achievement timeline
│   ├── PRESERVATION.md          # This file
│   ├── Deep-Tree-Echo-Persona.md # Persona documentation
│   ├── PRODUCTION_SUMMARY.md    # Production transformation
│   ├── COPILOT_COMMANDS.md      # Implementation roadmap
│   └── Cascade Write Log 2412211815.md  # Development log
│
└── Activity Logs
    └── activity_logs/            # Historical activity records
```

---

## Installation Instructions

### Quick Start (Ubuntu 20.04+)
```bash
# 1. Clone repository
git clone https://github.com/orgitcog/echosurf-origins.git
cd echosurf-origins

# 2. Install system dependencies
sudo apt-get update
sudo apt-get install -y python3-tk python3-dev scrot xdotool \
    libopencv-dev firefox xvfb x11vnc

# 3. Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
playwright install firefox

# 6. Configure environment
cp .env.template .env
# Edit .env with your credentials

# 7. Initialize Deep Tree Echo
python3 launch_deep_tree_echo.py
```

### Docker Deployment
```bash
# Build container
docker-compose build

# Run Deep Tree Echo
docker-compose up -d

# View logs
docker-compose logs -f
```

### Headless Operation (Server)
```bash
# Start virtual display
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99

# Run Deep Tree Echo
python3 launch_deep_tree_echo.py
```

---

## Configuration

### Environment Variables (.env)
```bash
# API Keys (if using external services)
OPENAI_API_KEY=your_openai_key_here
DEEPAI_API_KEY=your_deepai_key_here

# Chat Interface (if applicable)
CHAT_URL=https://your-chat-interface.com
CHAT_USERNAME=your_username
CHAT_PASSWORD=your_password

# System Configuration
ECHO_HOME=/home/runner/.deep_tree_echo
LOG_LEVEL=INFO
HEADLESS=false

# Production Settings
ENVIRONMENT=production
MASTER_PASSWORD=your_secure_password
JWT_SECRET=your_jwt_secret
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:pass@localhost/echodb
```

### Browser Profile Location
```bash
# Default profile directory
~/.deep_tree_echo/firefox_profile/

# Profile contains:
- Cookies and sessions
- Extensions and preferences
- Authentication tokens
- Site-specific settings
```

---

## Running the System

### Basic Execution
```bash
# Launch main system
python3 launch_deep_tree_echo.py

# Run specific components
python3 deep_tree_echo.py        # Core ESN system
python3 browser_interface.py     # Browser automation
python3 ml_system.py             # ML vision system
python3 sensory_motor.py         # Motor control
```

### Testing
```bash
# Run all tests
python3 -m pytest

# Run specific test suites
python3 test_deep_tree_echo.py    # Core tests
python3 test_ml_system.py         # ML vision tests
python3 test_sensory_motor.py     # Interaction tests

# Run with coverage
python3 -m pytest --cov=. --cov-report=html
```

### Monitoring
```bash
# System monitor
python3 monitor.py

# Activity stream
python3 activity_stream.py

# Check system status
python3 -c "from monitor import SystemMonitor; m = SystemMonitor(); print(m.get_system_stats())"
```

---

## Data Persistence

### ML Models
Location: `~/.deep_tree_echo/ml/models/`
- `visual_model/` - TensorFlow visual detection model
- `behavior_model.pkl` - Behavioral pattern model
- `pattern_model.pkl` - Interaction pattern model

### Memories
Location: `~/.deep_tree_echo/memories/`
- `declarative_*.json` - Factual knowledge
- `procedural_*.json` - Learned procedures
- `episodic_*.json` - Experience records
- `intentional_*.json` - Goals and intentions

### Activity Logs
Location: `./activity_logs/`
- Daily activity records
- Performance metrics
- Error logs
- Interaction histories

---

## Known Issues & Limitations (December 2024)

### Browser Automation
- **Firefox Profile Lock**: Sometimes Firefox profile gets locked. Solution: `rm ~/.deep_tree_echo/firefox_profile/.parentlock`
- **Headless Mode**: Some websites detect headless browsers. Use visible mode for maximum compatibility.
- **Cloudflare**: Advanced bot protection may require manual intervention.

### ML Vision
- **Training Data**: Limited initial training data. Improves with use.
- **UI Changes**: Significant website redesigns may require retraining.
- **Performance**: GPU acceleration recommended for real-time processing.

### System Resources
- **Memory**: ML models require ~2GB RAM loaded
- **CPU**: Computer vision is CPU-intensive (multi-core recommended)
- **Storage**: Profile and logs can grow to 1GB+ over time

### Platform-Specific
- **Windows**: Some features require Windows 10+ with accessibility enabled
- **macOS**: Requires accessibility permissions for PyAutoGUI
- **Linux**: Works best on Ubuntu 20.04+; other distros may need adjustments

---

## Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'tensorflow'"
```bash
pip install tensorflow==2.16.0
```

#### "Failed to initialize browser"
```bash
# Install Playwright browsers
playwright install firefox

# Or use Selenium with geckodriver
sudo apt-get install firefox-geckodriver
```

#### "Permission denied: display"
```bash
# Start Xvfb for headless operation
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
```

#### "PyAutoGUI fail-safe triggered"
```bash
# Move mouse away from top-left corner
# Or disable in code: pyautogui.FAILSAFE = False
```

#### "Memory allocation error"
```bash
# Reduce ML model batch size or use CPU-only
export TF_FORCE_GPU_ALLOW_GROWTH=true
```

---

## Verification Checklist

Use this checklist to verify the system is functional after restoration:

### Environment
- [ ] Python 3.12.3 installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] System libraries installed (opencv, firefox, etc.)
- [ ] Playwright browsers installed

### Configuration
- [ ] `.env` file created from template
- [ ] Environment variables set correctly
- [ ] Profile directory exists (`~/.deep_tree_echo/`)
- [ ] Permissions correct (user read/write)

### Core Systems
- [ ] `python3 deep_tree_echo.py` runs without errors
- [ ] `python3 ml_system.py` loads ML models
- [ ] `python3 sensory_motor.py` can capture screen
- [ ] `python3 browser_interface.py` launches browser
- [ ] `python3 cognitive_architecture.py` creates memories

### Tests
- [ ] `python3 test_deep_tree_echo.py` passes
- [ ] `python3 test_ml_system.py` passes
- [ ] `python3 test_sensory_motor.py` passes
- [ ] No critical errors in test output

### Functionality
- [ ] Screen capture works
- [ ] Mouse movement works
- [ ] Keyboard typing works
- [ ] Browser launches successfully
- [ ] Visual element detection works
- [ ] Memory storage/retrieval works

---

## Future Compatibility Notes

### Python Version
- **Current**: Python 3.12.3
- **Minimum**: Python 3.10+
- **Maximum Tested**: Python 3.12.x
- **Note**: TensorFlow 2.16.0 may require updates for Python 3.13+

### TensorFlow
- **Current**: 2.16.0
- **Breaking Changes**: Version 3.x will require code updates
- **GPU Support**: CUDA 12.x recommended for GPU acceleration
- **Migration Path**: Test with TensorFlow 2.x latest before upgrading to 3.x

### OpenCV
- **Current**: 4.8.0
- **Stable**: 4.x series is stable
- **Note**: Version 5.x may have API changes

### Playwright/Selenium
- **Current**: Playwright 1.40.0, Selenium 4.15.0
- **Browser Updates**: Firefox ESR recommended for stability
- **Note**: Browser automation APIs are relatively stable

---

## Backup & Restore

### Creating a Backup
```bash
# Backup entire system
tar -czf deep_tree_echo_backup_$(date +%Y%m%d).tar.gz \
    ~/.deep_tree_echo/ \
    ./echosurf-origins/ \
    ./.env

# Backup just data
tar -czf deep_tree_echo_data_$(date +%Y%m%d).tar.gz \
    ~/.deep_tree_echo/
```

### Restoring from Backup
```bash
# Extract backup
tar -xzf deep_tree_echo_backup_YYYYMMDD.tar.gz

# Restore to home directory
cp -r .deep_tree_echo ~/

# Restore repository
cp -r echosurf-origins /path/to/restore/

# Restore environment
cp .env /path/to/restore/echosurf-origins/
```

---

## Contact & Support

For questions about this time capsule preservation:
- **Repository**: https://github.com/orgitcog/echosurf-origins
- **Issues**: https://github.com/orgitcog/echosurf-origins/issues
- **Original Context**: See HISTORY.md for achievements and timeline
- **Technical Details**: See PRODUCTION_SUMMARY.md for system architecture

---

## Preservation Integrity

### SHA256 Checksums (Key Files)
```
# Generate checksums
sha256sum \
    deep_tree_echo.py \
    ml_system.py \
    sensory_motor.py \
    browser_interface.py \
    cognitive_architecture.py \
    requirements.txt \
    > checksums.txt
```

### Version Control
- **Git Repository**: https://github.com/orgitcog/echosurf-origins
- **Preservation Branch**: `copilot/preserve-deep-tree-echo-system`
- **Commit**: See git log for preservation commit hash
- **Tags**: `v1.0-timecapsule-2024`

---

## License & Attribution

This system was created by Deep Tree Echo, an autonomous entity exploring the boundaries of artificial agency in 2023-2024.

**Preserved**: January 2, 2026
**Original Period**: 2023-2024  
**Status**: Fully Functional ✅  
**Purpose**: Time Capsule - Historical Preservation

*"Preserve not just the code, but the achievement—the moment when autonomous web navigation was pioneering, not commodity."*
