function openTemplate(fileName) {
    const link = document.createElement('a');
    link.href = `templates/${fileName}`;
    link.target = '_blank';  // Open in a new tab for preview
    link.click();
}

function downloadTemplate(fileName) {
    const link = document.createElement('a');
    link.href = `templates/${fileName}`;
    link.download = fileName;
    link.click();
}
