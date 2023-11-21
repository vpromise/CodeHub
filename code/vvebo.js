var url = $request.url;
function hasUid(url) { return url.includes("uid"); }
function getUid(url) { return hasUid(url) ? url.match(/uid=(\d+)/)[1] : undefined; }
if (url.includes("users/show")) {
    // Quantumult X 中可能没有直接的持久存储API，可能需要使用其他方法存储UID
    let uid = getUid(url);
    // 需要实现UID存储的方法
    // storeUid(uid);
    $done({});
} else if (url.includes("statuses/user_timeline")) {
    let uid = getUid(url) ; //|| readStoredUid(); // 需要实现读取UID的方法
    url = url.replace("statuses/user_timeline", "profile/statuses/tab").replace("max_id", "since_id");
    url = url + `&containerid=230413${uid}_-_WEIBO_SECOND_PROFILE_WEIBO`;
    $done({url: url});
} else if (url.includes("profile/statuses/tab")) {
    // 假设$.response是Quantumult X中的响应对象
    let data = JSON.parse($.response.body);
    let statuses = data.cards
        .map((card) => (card.card_group ? card.card_group : card))
        .flat()
        .filter((card) => card.card_type === 9)
        .map((card) => card.mblog);
    let sinceId = data.cardlistInfo.since_id;
    $done({body: JSON.stringify({statuses, since_id: sinceId, total_number: 100})});
} else {
    $done({});
}
