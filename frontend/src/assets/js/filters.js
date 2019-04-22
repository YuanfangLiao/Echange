export function timeFormat (time) {
  let date = new Date(time)// 把定义的时间赋值进来进行下面的转换
  let year = date.getFullYear()
  let month = date.getMonth() + 1
  let day = date.getDate()
  let hour = date.getHours()
  let minute = date.getMinutes()
  let second = date.getSeconds()
  return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
}
