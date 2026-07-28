export function widgetPrice(qty) {
  if (qty <= 0) throw new Error("qty must be positive")
  return qty * 4.5
}

console.log("widget-api up")
