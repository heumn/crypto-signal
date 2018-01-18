#!/usr/local/bin/python
"""Main app module
"""

import time

import logs
import conf
import structlog

from behaviour import Behaviour

def main():
    """Initializes the application
    """
     # Load settings and create the config object
    config = conf.Configuration()
    settings = config.settings

    # Set up logger
    logs.configure_logging(settings['loglevel'], settings['log_mode'])
    logger = structlog.get_logger()

    # Configure and run configured behaviour.
    behaviour_manager = Behaviour(config)
    behaviour = behaviour_manager.get_behaviour(settings['selected_task'])

    while True:
        behaviour.run(settings['market_pairs'])
        logger.info("Sleeping for %s seconds", settings['update_interval'])
        time.sleep(settings['update_interval'])


if __name__ == "__main__":
    main()
