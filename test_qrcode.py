from promptpay import qrcode

def gen_qr(id_or_phone_number,money):
    payload = qrcode.generate_payload(id_or_phone_number)
    payload_with_amount = qrcode.generate_payload(id_or_phone_number, money)
    # export to PIL image
    # img = qrcode.to_image(payload)
    qrcode.to_file(payload_with_amount, "imgs/scanforpay.png")


gen_qr('0805471749',2)


# # generate a payload
# id_or_phone_number = "0841234567"
# payload = qrcode.generate_payload(id_or_phone_number)
# payload_with_amount = qrcode.generate_payload(id_or_phone_number, 1.23)

# # export to PIL image
# img = qrcode.to_image(payload)

# # export to file
# # qrcode.to_file(payload, "./qrcode-0841234567.png")
# qrcode.to_file(payload_with_amount, "qrcode-0841234567.png")