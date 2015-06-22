# Change log
All notable changes to this project will be documented in this file.
The project currently has no version numbering.
The following subheaders should be used in the change log: 

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for once-stable features removed in upcoming releases.
- `Removed` for deprecated features removed in this release.
- `Fixed` for any bug fixes.
- `Security` to invite users to upgrade in case of vulnerabilities.


## [wip] 2015-

## [maintentance] 2015-06-22
### Added
- Added "J.A. pripps Pub" restaurant module 

## [maintentance] 2015-05-04
### Added
- Added argparser
- Added "Bamjam Place" and "Pasta Etc." to the Other restaurant module.

### Changed
- Moved externally read configuration values into
  defaults in the command line arguments.

### Removed
- Removed unecessary dependencies on external files (other.txt, smptserver.txt)
  by moving defaults into argparser defaults.


## [maintenance] 2015-03-09
### Added
- Added restaurant module for Thai
- Support for changing the smtp server port used when sending emails.

### Fixed
- Changed to unicode strings in restaurant modules with "exotic" character
  requirements.


## [First release] 2015-03-06
### Added
- A restaurants module with modules for: Einstein, Kårrestaurangen, Linsen,
- Other, Pizza, Time Out Bistro, Chalmersvillan.
- Capability of sending emails to a list of email addresses.
- A README file with instructions on how to contribute.
- A Changelog file, where we keep notable modifications to the project.

