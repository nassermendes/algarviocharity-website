# Changelog

All notable changes to the Algarvio Charity website will be documented in this file.

## [2.0.0] - 2025-02-08

### Added
- Heroku deployment configuration
- Automatic SSL certificate management
- Custom domain support (algarviocharity.org)
- Environment variables for secure configuration

### Changed
- Migrated from GitHub Pages to Heroku hosting
- Updated all dependencies to latest versions
- Improved repository structure and organization

### Removed
- Old deployment scripts and configurations
- Unnecessary build artifacts and cache files
- GitHub Pages configuration

### Security
- Updated all dependencies to latest secure versions
- Implemented secure email configuration
- Added comprehensive .gitignore rules

### Technical Details
- Commit: 7cc563dce04ebfcc5506cfb038107bb0eb2401ce
- Branch: main
- Dependencies:
  - Flask==3.0.2
  - Flask-Bootstrap==3.3.7.1
  - Flask-Mail==0.9.1
  - Flask-SQLAlchemy==3.1.1
  - Jinja2==3.1.2
  - SQLAlchemy==2.0.38
  - Werkzeug==3.0.1
  - gunicorn==21.2.0
  - python-dotenv==1.0.0

## [1.4] - 2025-02-07
### Changed
- Updated card styling to match dark theme
- Enhanced card visual appearance with transparent background
- Improved text colors for better readability
- Refined card hover effects

## [1.3] - 2025-02-07
### Changed
- Enhanced About page content with more detailed information
- Added "How We Operate" section to About page
- Updated mission statement and values descriptions
- Refined service descriptions for better clarity

## [1.2] - 2025-02-07
### Changed
- Updated card background color to #77725b for improved visual consistency

## [1.1] - 2025-02-07
### Changed
- Updated banner image path for better organization
- Fixed image paths to use correct filenames
- Improved file structure and organization

## [1.0] - 2025-02-06
### Initial Release
- Basic website structure with home, about, services, and contact pages
- Implemented hero section with logo and banner
- Added mission statement section
- Created services section with cards
- Integrated values section
- Added contact form functionality
- Implemented responsive design
- Set up initial color scheme and typography
