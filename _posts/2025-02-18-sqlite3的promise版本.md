---
title: "sqlite3的promise版本"
date: "2025-02-18"
categories: 
  - "javascript"
---

```
import { Database } from 'sqlite3'
export var db

// exports.db = db

export function sqlite_open(path) {
  return new Promise(function (resolve, reject) {
    db = new Database(path, function (err) {
      if (err) reject('Open error: ' + err.message)
      else resolve(path + ' opened')
    })
  })
}

// any query: insert/delete/update
export function sqlite_run(query) {
  return new Promise(function (resolve, reject) {
    db.run(query, function (err) {
      if (err) reject(err.message)
      else resolve(true)
    })
  })
}

// first row read
export function sqlite_get(query, params) {
  return new Promise(function (resolve, reject) {
    db.get(query, params, function (err, row) {
      if (err) reject('Read error: ' + err.message)
      else {
        resolve(row)
      }
    })
  })
}

// set of rows read
export function sqlite_all(query, params) {
  return new Promise(function (resolve, reject) {
    if (params == undefined) params = []

    db.all(query, params, function (err, rows) {
      if (err) reject('Read error: ' + err.message)
      else {
        resolve(rows)
      }
    })
  })
}

// each row returned one by one
export function sqlite_each(query, params, action) {
  return new Promise(function (resolve, reject) {
    var db = db
    db.serialize(function () {
      db.each(query, params, function (err, row) {
        if (err) reject('Read error: ' + err.message)
        else {
          if (row) {
            action(row)
          }
        }
      })
      db.get('', function (err, row) {
        resolve(true)
      })
    })
  })
}

export function sqlite_close() {
  return new Promise(function (resolve, reject) {
    db.close()
    resolve(true)
  })
}

```
