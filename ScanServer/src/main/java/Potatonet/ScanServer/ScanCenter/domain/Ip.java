package Potatonet.ScanServer.ScanCenter.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Index;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Component
@Table(name = "IP", indexes = {
        @Index(name = "ip_crc_idx", columnList = "ip_crc")
})
public class Ip {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ip_id")
    private Long ipId;

    @Column(name = "ip", nullable = false, unique = true)
    private String ip;

    @Column(name = "ip_crc", nullable = false)
    private Long ipCrc;

    @Column(name = "create_time", nullable = false)

    private java.util.Date createTime;

    // 생성자, getter, setter 등 필요한 메서드들을 추가



    // getter, setter 등 필요한 메서드들을 추가
}

