var url = $request.url;
var headers = $request.headers;

function hasUid(url) { return url.includes("uid"); }
function getUid(url) { return hasUid(url) ? url.match(/uid=(\d+)/)[1] : undefined; }

if (url.includes("users/show")) {
  let uid = getUid(url);
  if (uid) {
    $prefs.setValueForKey(uid, "uid");
    $done({});
  }
} else if (url.includes("statuses/user_timeline")) {
  let uid = getUid(url) || $prefs.valueForKey("uid");
  if (uid) {
    url = url.replace("statuses/user_timeline", "profile/statuses/tab").replace("max_id", "since_id");
    url = url + `&containerid=230413${uid}_-_WEIBO_SECOND_PROFILE_WEIBO`;
    $done({ url: url });
  } else {
    $done({});
  }
} else if (url.includes("profile/statuses/tab")) {
  let body = $response.body;
  let obj = JSON.parse(body);
  let statuses = obj.cards
    .map((card) => (card.card_group ? card.card_group : card))
    .flat()
    .filter((card) => card.card_type === 9)
    .map((card) => card.mblog);
  let sinceId = obj.cardlistInfo.since_id;
  body = JSON.stringify({ statuses, since_id: sinceId, total_number: 100 });
  $done({ body: body });
} else {
  $done({});
}
