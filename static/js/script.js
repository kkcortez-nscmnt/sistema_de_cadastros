$("#table").DataTable({
  // Datatables configurações
  paging: true, // Pagination
  pageLength: 10, // Data por página
  lengthChange: true, // entradas por página
  searching: true, // formulario de pesquisa
  bInfo: true, //
  bSort: true,
  // desabilita ordenação e colunas epecificas
  "columnDefs": [
    {
      "targets": 5,
      "orderable": false,
    }
  ]
});
$(document).ready(function () {
  // Este código será executado após o carregamento completo do DOM
  let newSearch = $("#table").DataTable();
  $('#search').keyup(function () {
    newSearch.search($(this).val()).draw();
  });
});

