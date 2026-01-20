```

#!/bin/bash

# Kiểm tra quyền root
if [[ $EUID -ne 0 ]]; then
   echo "Vui lòng chạy script với quyền sudo hoặc root!"
   exit 1
fi

echo "==============================================="
echo "   HỆ THỐNG CÀI ĐẶT MARIADB REPLICATION"
echo "==============================================="
echo "1. Cấu hình máy MASTER (192.168.88.151)"
echo "2. Cấu hình máy SLAVE  (192.168.88.152)"
echo "3. Thoát"
read -p "Lựa chọn của bạn (1-3): " CHOICE

case $CHOICE in
    1)
        echo "--- ĐANG CẤU HÌNH MASTER ---"
        read -p "Nhập IP của máy SLAVE: " SLAVE_IP
        read -sp "Thiết lập mật khẩu cho user REPLICA: " REPL_PW
        echo ""
        read -sp "Thiết lập mật khẩu CHUNG cho user IPTV: " IPTV_PW
        echo ""

        echo "1. Cài đặt MariaDB Server..."
        dnf install -y mariadb-server

        echo "2. Cấu hình /etc/my.cnf.d/replication.cnf..."
        cat <<EOF > /etc/my.cnf.d/replication.cnf
[mariadb]
log-bin = master1-bin
server-id = 1
bind-address = 0.0.0.0
EOF

        echo "3. Khởi động dịch vụ và mở Firewall..."
        systemctl enable --now mariadb
        firewall-cmd --permanent --add-service=mysql
        firewall-cmd --reload

        echo "4. Tạo các user hệ thống..."
        # User để Slave đồng bộ dữ liệu
        mysql -e "CREATE USER IF NOT EXISTS 'replica'@'$SLAVE_IP' IDENTIFIED BY '$REPL_PW';"
        mysql -e "GRANT REPLICATION SLAVE ON *.* TO 'replica'@'$SLAVE_IP';"
        
        # User IPTV (Sẽ tự đồng bộ sang Slave)
        mysql -e "CREATE USER IF NOT EXISTS 'iptv'@'%' IDENTIFIED BY '$IPTV_PW';"
        mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'iptv'@'%';"
        
        mysql -e "FLUSH PRIVILEGES;"

        echo "-----------------------------------------------"
        echo "CÀI ĐẶT MASTER HOÀN TẤT!"
        echo "Lưu thông số sau để nhập vào máy Slave:"
        mysql -e "SHOW MASTER STATUS;"
        ;;

    2)
        echo "--- ĐANG CẤU HÌNH SLAVE ---"
        read -p "Nhập IP của máy MASTER: " MASTER_IP
        read -sp "Nhập mật khẩu REPLICA đã tạo trên Master: " MASTER_PW
        echo ""
        read -p "Nhập File log (ví dụ: master1-bin.000001): " LOG_FILE
        read -p "Nhập Position (ví dụ: 330): " LOG_POS

        echo "1. Cài đặt MariaDB Server..."
        dnf install -y mariadb-server

        echo "2. Cấu hình Slave với chế độ Read-Only..."
        cat <<EOF > /etc/my.cnf.d/replication.cnf
[mariadb]
server-id = 2
read_only = 1
EOF

        echo "3. Khởi động lại dịch vụ..."
        systemctl restart mariadb
        systemctl enable mariadb

        echo "4. Kết nối tới Master..."
        mysql -e "STOP SLAVE;"
        mysql -e "CHANGE MASTER TO MASTER_HOST='$MASTER_IP', MASTER_USER='replica', MASTER_PASSWORD='$MASTER_PW', MASTER_LOG_FILE='$LOG_FILE', MASTER_LOG_POS=$LOG_POS;"
        mysql -e "START SLAVE;"

        echo "-----------------------------------------------"
        echo "KIỂM TRA TRẠNG THÁI:"
        mysql -e "SHOW SLAVE STATUS\G" | grep -E "Slave_(IO|SQL)_Running|Seconds_Behind_Master"
        echo "Lưu ý: User 'iptv' đã có sẵn và sẽ chỉ có quyền ĐỌC trên máy này."
        ;;

    3)
        exit 0
        ;;
    *)
        echo "Lựa chọn không hợp lệ!"
        ;;
esac

```
