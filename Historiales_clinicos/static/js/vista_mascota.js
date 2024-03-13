// JavaScript para la búsqueda en la tabla
const searchInput = document.querySelector('.table__header .input_group input');
const tableRows = document.querySelectorAll('.table__body tbody tr');

searchInput.addEventListener('input', searchTable);

function searchTable() {
    const searchValue = searchInput.value.trim().toLowerCase();

    tableRows.forEach((row, i) => {
        const rowData = row.textContent.toLowerCase();
        row.classList.toggle('hide', rowData.indexOf(searchValue) === -1);
        row.style.setProperty('--delay', i / 25 + 's');
    });

    // Aplicar estilos a las filas visibles
    document.querySelectorAll('.table__body tbody tr:not(.hide)').forEach((visibleRow, i) => {
        visibleRow.style.backgroundColor = i % 2 === 0 ? 'transparent' : 'rgba(0, 0, 0, 0.05)';
    });
}


