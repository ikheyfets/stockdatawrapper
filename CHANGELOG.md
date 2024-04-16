# Change Log

## [0.2.1] - 2024-04-16

### Added

### Changed

* renamed *wrapper.py* to *stockdatawrapper.py* for a better import statement 

### Fixed

* *validation.json* is now included in pyproject.toml, so the package is operational after building it with `poetry build`

## [0.2.0] - 2024-04-08

### Added

* Added methods covered in the Stock Splits and Dividents section of the API doc to StockDataApiWrapper class and corresponding criteria in ./wrapper/validation.json
* Added validation for range-based arguments for current and future endpoints
* Added a way for UUIDs to be added to the API call

### Changed

### Fixed

## [0.1.0] - 2024-04-08

### Added

* Established general project structure
* Request validation against ./wrapper/validation.json to check for acceptable parameters and corresponding datatypes.
* Added methods covered in the Stock Data Prices section to StockDataApiWrapper class.

### Changed

### Fixed
