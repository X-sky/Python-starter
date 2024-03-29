from operator import itemgetter

import requests

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()


def get_submission_dict(submission_id):
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        "title": "",
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": 0,
    }
    try:
        title, comments = itemgetter("title", "descendants")(response_dict)
    except KeyError:
        print(f"missing data for id: {submission_id}")
    else:
        submission_dict["title"] = title
        submission_dict["comments"] = comments

    return submission_dict


submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    submission_dicts.append(get_submission_dict(submission_id))

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

texts = ""
for submission_dict in submission_dicts:
    texts += f"\nTitle: {submission_dict['title']}"
    texts += f"Discussion link: {submission_dict['hn_link']}"
    texts += f"Comments: {submission_dict['comments']}"

with open("test.txt", "w") as f:
    f.write(texts)
