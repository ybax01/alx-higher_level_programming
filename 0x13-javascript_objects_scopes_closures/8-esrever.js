#!/usr/bin/node

exports.esrever = function (list) {
  if (list === undefined) return [];
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
