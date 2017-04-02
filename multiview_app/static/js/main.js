// Sidebars
$(document).ready(function () {
  // Initialize collapse button
  $(".button-collapse").sideNav();
  // Updating Form fields
  Materialize.updateTextFields();
  // Initialize data tables
  var table = $("#data-table").DataTable({
    "bLengthChange": false,
  });
  table.column('2:visible').order('desc').draw();
});
