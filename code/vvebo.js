const url = $request.url;

function rewriteUserShow(url) {
  const uid = url.match(/uid=(\d+)/)[1];
  if (uid) {
    $prefs.setValueForKey(uid, "uid");
  }
  $done({});
}

function rewriteUserTimeline(url) {
  const uid = $prefs.valueForKey("uid");
  let modifiedUrl = url.replace("statuses/user_timeline", "profile/statuses/tab").replace("max_id", "since_id");
  modifiedUrl += `&containerid=230413${uid}_-_WEIBO_SECOND_PROFILE_WEIBO`;
  $done({ url: modifiedUrl });
}

function rewriteProfileStatusesTab(body) {
  const data = JSON.parse(body);
  const statuses = data.cards
    .map(card => card.card_group ? card.card_group : card)
    .flat()
    .filter(card => card.card_type === 9)
    .map(card => card.mblog);
  const sinceId = data.cardlistInfo.since_id;
  $done({ body: JSON.stringify({ statuses, since_id: sinceId, total_number: 100 }) });
}

if (url.includes("users/show")) {
  rewriteUserShow(url);
} else if (url.includes("statuses/user_timeline")) {
  rewriteUserTimeline(url);
} else if (url.includes("profile/statuses/tab")) {
  const body = $response.body;
  rewriteProfileStatusesTab(body);
} else {
  $done({});
}
