let url = $request.url;

// 从URL中提取UID
function getUid(url) {
  let uidMatch = url.match(/uid=(\d+)/);
  return uidMatch ? uidMatch[1] : null;
}

// 重写请求，将statuses/user_timeline的请求转换为profile/statuses/tab的请求
if (url.includes("statuses/user_timeline")) {
  let uid = getUid(url);
  if (uid) {
    let modifiedUrl = url.replace("statuses/user_timeline", "profile/statuses/tab")
                         .replace("max_id", "since_id")
                         .replace(/feature=\d+/g, "");  // 移除feature参数，如果有的话
    modifiedUrl += `&containerid=230413${uid}_-_WEIBO_SECOND_PROFILE_WEIBO`;
    $done({ url: modifiedUrl });
  } else {
    $done({});
  }
} else if (url.includes("profile/statuses/tab")) {
  // 处理响应体，将其转换为statuses/user_timeline格式
  let body = $response.body;
  const data = JSON.parse(body);
  const statuses = data.cards
    .map(card => card.card_group ? card.card_group : card)
    .flat()
    .filter(card => card.card_type === 9)
    .map(card => card.mblog);
  const sinceId = data.cardlistInfo.since_id;
  // 构建原始的statuses/user_timeline响应格式
  let originalFormat = {
    statuses: statuses,
    since_id: sinceId,
    total_number: data.cardlistInfo.total_number || 100
  };
  $done({ body: JSON.stringify(originalFormat) });
} else {
  // 如果URL不包含上述两种情况，则不修改
  $done({});
}
