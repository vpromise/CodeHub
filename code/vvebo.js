var url = $request.url;

function hasUid(url) {
  return url.includes("uid");
}

function getUid(url) {
  return hasUid(url) ? url.match(/uid=(\d+)/)[1] : undefined;
}

if (url.includes("users/show")) {
  $prefs.setValueForKey(getUid(url), "uid");
  $done({});
} else if (url.includes("statuses/user_timeline")) {
  var uid = getUid(url) || $prefs.valueForKey("uid");
  url = url.replace("statuses/user_timeline", "profile/statuses/tab").replace("max_id", "since_id");
  url = url + `&containerid=230413${uid}_-_WEIBO_SECOND_PROFILE_WEIBO`;
  $done({ url: url });
} else if (url.includes("profile/statuses/tab")) {
  var data = JSON.parse($response.body);
  var statuses = data.cards
    .map(function(card) { return card.card_group ? card.card_group : card; })
    .flat()
    .filter(function(card) { return card.card_type === 9; })
    .map(function(card) { return card.mblog; });
  var sinceId = data.cardlistInfo.since_id;
  $done({ body: JSON.stringify({ statuses, since_id: sinceId, total_number: 100 }) });
} else {
  $done({});
}
