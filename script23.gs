function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu(“Facts”)
  .addItem(“2s”, ‘factsMake(1)’)
  .addItem(“3s”, ‘factsMake(3)’)
  .addItem(“4s”, ‘factsMake(4)’)
  .addItem(“5s”, ‘factsMake(5)’)
  .addItem(“6s”, ‘factsMake(6)’)
  .addItem(“7s”, ‘factsMake(7)’)
  .addItem(“8s”, ‘factsMake(8)’)
  .addItem(“9s”, ‘factsMake(9)’)
  .addSeparator()
  .addItem(“Check Facts”, “checkFacts”)
  .addToUi();
}
