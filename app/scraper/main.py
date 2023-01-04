import service.catalogue_service as catalogue_service
import logging
import datetime

logger = logging.getLogger('ScraperJob')

MANUFACTURER_URL = "index.cfm/page/catalogue"

def execute_job():
    final_data = []
    manufacturers_list = catalogue_service.fetch_item_list(MANUFACTURER_URL, 'c_container allmakes')

    for manufacturer,category_url in manufacturers_list.items():
        categories_list = catalogue_service.fetch_item_list(category_url, 'c_container allmakes allcategories')

        for category,model_url in categories_list.items():
            model_list = catalogue_service.fetch_item_list(model_url, 'c_container allmodels')

            for model,parts_url in model_list.items():
                parts_list = catalogue_service.get_parts(parts_url, 'c_container allparts')

                for part, part_category in parts_list.items():
                    catalogue_data = {}
                    catalogue_data["manufacturer"] = manufacturer
                    catalogue_data["category"] = category
                    catalogue_data["model"] = model
                    catalogue_data["part"] = part
                    catalogue_data["part_category"] = part_category
                    final_data.append(catalogue_data)                
        
    catalogue_service.save_catalogue(final_data)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    logger.info(f"Starting Updating Database. Start time: {start_time}")

    if execute_job() is True:
        end = datetime.datetime.now()
        logger.info(
            f"Updating Database jobs has been successfully completed . Execution time: {end - start_time}")
    else:
        logger.info("Something going Wrong. Unable to update database")