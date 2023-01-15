from bing_image_downloader import downloader
import concurrent.futures

def download_images(query, number_of_images):
    downloader.download(query, limit=number_of_images, output_dir='images', adult_filter_off=True, force_replace=False)

def main(queries, number_of_images):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda x: download_images(x, number_of_images), queries)

if __name__ == "__main__":
    queries = ["penguin in the wild", "giraffe in the wild", "racoon in the wild", "hippo in the wild", "parrot"]
    number_of_images = 200
    main(queries, number_of_images)
