$("#table").DataTable({
    // Datatables configurations
    paging: true,
    pageLength: 10,
    lengthChange: true,
    searching: true,
    bInfo: true,
    bSort: true,
    //desabilita ordenação e colunas epecificas
    "columnDefs": [{
        "targets": [4, 5, 6],
        "orderable": false
    }]
});
