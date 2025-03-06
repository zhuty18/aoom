function work_of (pages, slice_at) {
    return pages.where((x) => x.word_count && (x.file.path.indexOf("trash" < 0))).sort((x) => x.word_count, "desc").sort((x) => x.date ? x.date : x.auto_date, "desc").slice(0, slice_at)
}

function meter_at (value, home) {
    return `<meter value=${value} min=0 max=1 low=${home.percent_low} high=${home.percent_high} optimum=${home.percent_ideal}></meter>`
}
function count (x) {
    return Math.max(x.word_count, Math.round(x.file.size / 3 - Math.min(x.file.size / 6, Math.max(50, x.file.size / 200))))
}
function count_meter (x, home) {
    if (x.file.tags.includes("#FIN")) {
        return meter_at(1,home)
    } else {
        let tmp = count(x)
        return meter_at(tmp / Math.max(tmp / home.percent_ideal, home.count_ideal), home)
    }
}
function last_update (x) {
    return Math.floor((Date.now() - Date.parse(x.date ? x.date : x.auto_date)) / 1000 / 60 / 60 / 24)
}
function last_update_str (x) {
    let days = last_update(x)
    if (days == 0) {
        return "今天"
    } else if (days == 1) {
        return "昨天"
    } else if (days == 2) {
        return "前天"
    } else {
        return days + "天前"
    }
}
function pin_of (x, home) {
    return "- [" + ((last_update(x) < Number(home.day_ideal)) ? "f" : "n") + "] "
}

function short_text (x, home, tag_number = 2) {
    return pin_of(x, home) + x.file.link + x.file.tags.filter((y) => y != "#FIN").slice(0, tag_number).join(" ") + count_meter(x, home)
}

exports.short_text = short_text
exports.work_of = work_of
exports.last_update = last_update
exports.last_update_str = last_update_str
exports.count = count
exports.count_meter = count_meter
exports.pin_of = pin_of
