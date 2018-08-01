import os
from icloudpd.logger import setup_logger
from icloudpd.paths import local_download_path


def autodelete_photos(icloud, folder_structure, directory):
    logger = setup_logger()
    logger.info("Deleting any files found in 'Recently Deleted'...")

    recently_deleted = icloud.photos.albums["Recently Deleted"]

    for media in recently_deleted:
        created_date = media.created
        date_path = folder_structure.format(created_date)
        download_dir = os.path.join(directory, date_path)

        for size in [None, "original", "medium", "thumb"]:
            path = local_download_path(media, size, download_dir)
            if os.path.exists(path):
                logger.info("Deleting %s!" % path)
                os.remove(path)
