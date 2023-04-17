const patientBtn = document.getElementById('patient-btn');
const imageBtn = document.getElementById('image-btn');
const resultDiv = document.getElementById('result');

// Get patient name
patientBtn.addEventListener('click', async () => {
    const response = await fetch('/dicom/patient', { method: 'GET' });
    const data = await response.json();
    resultDiv.innerHTML = `Patient Name: ${data.name}`;
});

// Get image
imageBtn.addEventListener('click', async () => {
    const response = await fetch('/dicom/image', { method: 'GET' });
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    resultDiv.innerHTML = `<img src="${url}" alt="DICOM Image"/>`;
});
