import pkg_resources
try:
    version = pkg_resources.get_distribution("pyramid").version
    print("Pyramid version:", version)
except pkg_resources.DistributionNotFound:
    print("Pyramid is not installed.")
