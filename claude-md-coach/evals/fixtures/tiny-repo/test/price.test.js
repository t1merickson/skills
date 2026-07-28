import { test } from "node:test"
import assert from "node:assert"
import { widgetPrice } from "../src/index.js"

test("widgetPrice scales", () => {
  assert.strictEqual(widgetPrice(2), 9)
})
