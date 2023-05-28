from scraper.oreilly_scraper import OreillyScraper

data = """
{"count":11,"next":"https://learning.oreilly.com/api/v1/reports/25502/?page=2","previous":null,"results":[{"id":104339,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2021-11-10T23:08:33.639000Z","source":"heron","rating":"5.000","comment":"Really useful. MLops is pretty fluid right now, but this is great for a foundation.","screen_name":"makotoblasa","uuid_user_id":"ef6b0d82-9292-4b7d-a4aa-b2084cbff804"},{"id":103721,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2021-10-07T11:15:52.313000Z","source":"heron","rating":"3.000","comment":"MLOps in Theory ","screen_name":"varunkumarnomula","uuid_user_id":"16cbb4e7-8988-41f9-819b-b6d917136745"},{"id":101393,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2021-06-10T19:48:53.569000Z","source":"heron","rating":"5.000","comment":"great book","screen_name":"khaoulakadri","uuid_user_id":"57866267-67a4-4346-bad2-ab686f7676db"},{"id":101026,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2021-05-20T20:22:54.669000Z","source":"heron","rating":"1.000","comment":"<p>Only theory, nothing practical.</p>\n","screen_name":"karishmaminkalainen","uuid_user_id":"cfbacc2a-86ce-4178-870b-77c97fc6f7f4"},{"id":97622,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-12-01T13:24:28.631000Z","source":"heron","rating":"4.500","comment":"<p>I read 5 chapters which are available so far. Good book which covered many important aspects of Ops in ML.</p>\n","screen_name":"rnandepu","uuid_user_id":"e7e77630-5916-4da0-b9db-e954e70d03fb"},{"id":97480,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-11-25T05:54:33.758000Z","source":"heron","rating":"2.000","comment":"<p>The first and the last chapters were helpful but most of the book is talking about the common data science topics. </p>","screen_name":"enginkapti","uuid_user_id":"69836b18-e476-4faa-8668-1e866790fee6"},{"id":97427,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-11-22T23:07:33.862000Z","source":"heron","rating":"5.000","comment":"<p>Nice work. Can you upload more chapters? That would be great. Thanks</p>","screen_name":"wajeehulhassan","uuid_user_id":"853d8e6b-0c8e-42af-93d3-d0a32aa44211"},{"id":97358,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-11-19T21:12:10.427000Z","source":"heron","rating":"2.000","comment":"","screen_name":"madhavkruthiventy","uuid_user_id":"06d9540c-b3a0-458c-8985-146736579450"},{"id":96016,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-09-18T12:09:22.404000Z","source":"heron","rating":"5.000","comment":"","screen_name":"nellaivijay","uuid_user_id":"cc7e4816-57e3-4050-9b3e-8efc96bf7de0"},{"id":95298,"report":"https://learning.oreilly.com/api/v1/reports/25502/","entity_id":"9781492083283","entity_type":"book","timestamp_created":"2020-08-17T06:57:32.643000Z","source":"heron","rating":"5.000","comment":"","screen_name":"smardirosians","uuid_user_id":"e068f141-92a2-4a29-80a8-3bde6d8381e0"}]}
"""

if __name__ == "__main__":
#     scraper = OreillyScraper()
#     scraper.scape_book_data()

    import json
    # with open(data, 'r') as file:
    
    review_list = []    
    endpoint_list = get_review_endpoints()

    def parsed_review_data(data):   
        if 'results' in data:
            review_info = {
                'id' : data['results']['id'],
                'entity_id': data['results']['entity_id'],
                'entity_type': data['results']['entity_type'],
                'timestamp_created': data['results']['timestamp_created'],
                'source': data['results']['source'],
                'rating': data['results']['rating'],
                'comment': data['results']['comment'],
                'screen_name': data['results']['screen_name'],
                'uuid_user_id': data['results']['uuid_user_id']
            }
        review_list.extend(review_info)
        return review_list

    while not endpoint_list:
        
        endpoint = endpoint_list.pop()
        response = requests.get(url=next_url, headers=headers, params=params)
        data = json.loads(response.text, strict=False)

        while True:
            if 'next' in data:
                next_url = data['next']
                headers = {}
                params = {}

                endpoint_list.append(next_url)
                response = requests.get(url=next_url, headers=headers, params=params)

                time.sleep(1)

                data = json.loads(response.text, strict=False)
            else:
                break
        
        if 'results' in data:
            review_info = {
                'id' : data['results']['id'],
                'entity_id': data['results']['entity_id'],
                'entity_type': data['results']['entity_type'],
                'timestamp_created': data['results']['timestamp_created'],
                'source': data['results']['source'],
                'rating': data['results']['rating'],
                'comment': data['results']['comment'],
                'screen_name': data['results']['screen_name'],
                'uuid_user_id': data['results']['uuid_user_id']
            }

            review_list.append(review_info)