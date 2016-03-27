import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='sportamore.log',
    filemode='w',
)

TIMEOUT = 10 # seconds
