import os
import shutil
import logging


def organiz_file(config) -> None:
    source_folder = config.get("source_folder")
    destination_folders = config.get("destination_folders", {})
    
    if not source_folder or not os.path.exists(source_folder):
        logging.error("Source folder does not exist.")
        return
    
    logging.info(f"Organizing files from {source_folder}")
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        

        if os.path.isfile(file_path):
            extension = filename.split('.')[-1].lower()
            destination = None

            if extension in ["jpg", "png", "gif"]:
                destination = destination_folders.get("images")
            elif extension in ["txt", "pdf", "docx"]:
                destination = destination_folders.get("documents")
            else:
                destination = destination_folders.get("others")

            if destination:
                if not os.path.exists(destination):
                    os.makedirs(destination)

                shutil.move(file_path, os.path.join(destination, filename))
                logging.info(f"Moved: {filename} -> {destination}")

    logging.info("File organization completed.")