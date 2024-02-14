# Scrapper
Module created to store all the posible web scrappers.

### Modules
1. **WS_MercadoLibre**: Initializes the main class with specified configurations for processing a list of words.

## Requirements
- Python 3.x
- pandas
- multiprocessing
- threading
- asyncio

## Usage

### WS_MercadoLibre
* **Initialization**:
    - `list_of_words` (list[str]): A list of words to be processed.
    - `cpu_cores_usage` (int, optional): Number of CPU cores to use. Defaults to half of the available cores if 'default' is specified.
    - `threads_limit` (int, optional): The limit of threads to use. Defaults to the number of available CPU cores if 'default' is specified.
    - `verbose` (bool, optional): If True, enables verbose output. Defaults to False.

* **Attributes**:
    - `verbose` (bool): Controls verbose output for debugging and monitoring.
    - `cpu_cores_usage` (int): Number of CPU cores to use for processing.
    - `threads_limit` (int): Maximum number of threads to use for processing.
    - `list_of_words` (list[str]): List of words to be processed.
    - `word_status_df` (pandas.DataFrame): DataFrame tracking the processing status of each word.

* **Methods**:
    - `start_subprocess`: Starts a subprocess for managing a set of threads.
    - `start`: Initiates the main processing workflow.